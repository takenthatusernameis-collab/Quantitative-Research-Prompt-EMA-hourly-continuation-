# EMA Hourly Continuation — DUSK/USDT P20_100

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.6376 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8866 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -3.8188 |
| sortino_ratio | -1.3775 |
| max_drawdown | 0.8161 |
| cagr | -0.4760 |
| net_avg_win | 47.5467 |
| net_avg_loss | -62.2145 |
| avg_hold_time_bars | 13.6340 |
| exposure | 0.4047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
