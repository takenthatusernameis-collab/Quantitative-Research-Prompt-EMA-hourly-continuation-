# EMA Hourly Continuation — NOT/USDT P26_100

**Symbol:** NOT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.8144 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 0.9882 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.3244 |
| sortino_ratio | -0.3956 |
| max_drawdown | 0.4106 |
| cagr | -0.1676 |
| net_avg_win | 75.1798 |
| net_avg_loss | -91.8718 |
| avg_hold_time_bars | 16.0808 |
| exposure | 0.3180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
