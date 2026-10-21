# EMA Hourly Continuation — INJ/USDT P12_50

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.8154 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0103 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7214 |
| sortino_ratio | -0.6170 |
| max_drawdown | 0.5403 |
| cagr | -0.2484 |
| net_avg_win | 72.2122 |
| net_avg_loss | -88.5641 |
| avg_hold_time_bars | 11.0495 |
| exposure | 0.3144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
