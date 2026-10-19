# EMA Hourly Continuation — ICP/USDT P26_55

**Symbol:** ICP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.4672 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8733 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -6.8543 |
| sortino_ratio | -2.9284 |
| max_drawdown | 0.9743 |
| cagr | -0.7651 |
| net_avg_win | 19.7221 |
| net_avg_loss | -37.2232 |
| avg_hold_time_bars | 4.1364 |
| exposure | 0.1737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
