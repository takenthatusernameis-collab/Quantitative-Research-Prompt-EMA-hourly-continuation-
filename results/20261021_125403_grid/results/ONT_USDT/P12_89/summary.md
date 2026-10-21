# EMA Hourly Continuation — ONT/USDT P12_89

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.7330 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -2.3982 |
| sortino_ratio | -0.7860 |
| max_drawdown | 0.6338 |
| cagr | -0.3042 |
| net_avg_win | 65.5566 |
| net_avg_loss | -79.3280 |
| avg_hold_time_bars | 21.0562 |
| exposure | 0.5088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
