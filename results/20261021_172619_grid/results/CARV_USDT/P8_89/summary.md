# EMA Hourly Continuation — CARV/USDT P8_89

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.8453 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0530 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.3029 |
| sortino_ratio | -0.4309 |
| max_drawdown | 0.4443 |
| cagr | -0.1818 |
| net_avg_win | 83.4398 |
| net_avg_loss | -102.4510 |
| avg_hold_time_bars | 25.2186 |
| exposure | 0.6102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
