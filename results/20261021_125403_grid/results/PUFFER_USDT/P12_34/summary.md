# EMA Hourly Continuation — PUFFER/USDT P12_34

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.8048 |
| net_win_rate | 0.5062 |
| gross_profit_factor | 1.0288 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -1.7222 |
| sortino_ratio | -0.6041 |
| max_drawdown | 0.4709 |
| cagr | -0.2435 |
| net_avg_win | 73.0334 |
| net_avg_loss | -93.0417 |
| avg_hold_time_bars | 7.8479 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
