# EMA Hourly Continuation — ROSE/USDT P12_200

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8796 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.1250 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -0.6178 |
| sortino_ratio | -0.1494 |
| max_drawdown | 0.2054 |
| cagr | -0.0693 |
| net_avg_win | 80.4186 |
| net_avg_loss | -101.5841 |
| avg_hold_time_bars | 62.1825 |
| exposure | 0.8055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
