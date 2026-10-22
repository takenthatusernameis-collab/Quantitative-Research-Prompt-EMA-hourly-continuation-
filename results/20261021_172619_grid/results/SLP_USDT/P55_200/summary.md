# EMA Hourly Continuation — SLP/USDT P55_200

**Symbol:** SLP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.8705 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0783 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.7355 |
| sortino_ratio | -0.1907 |
| max_drawdown | 0.2206 |
| cagr | -0.0866 |
| net_avg_win | 80.9283 |
| net_avg_loss | -100.7143 |
| avg_hold_time_bars | 25.2769 |
| exposure | 0.3734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
