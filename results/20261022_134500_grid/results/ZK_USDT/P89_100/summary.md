# EMA Hourly Continuation — ZK/USDT P89_100

**Symbol:** ZK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.3325 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.8165 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -7.6464 |
| sortino_ratio | -2.6920 |
| max_drawdown | 0.9639 |
| cagr | -0.7540 |
| net_avg_win | 18.8790 |
| net_avg_loss | -44.9226 |
| avg_hold_time_bars | 2.8817 |
| exposure | 0.0808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
