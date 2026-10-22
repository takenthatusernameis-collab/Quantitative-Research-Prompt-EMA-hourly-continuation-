# EMA Hourly Continuation — AVAX/USDT P26_144

**Symbol:** AVAX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.6645 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 1.0245 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -3.1886 |
| sortino_ratio | -0.9824 |
| max_drawdown | 0.7245 |
| cagr | -0.3721 |
| net_avg_win | 59.3462 |
| net_avg_loss | -83.1673 |
| avg_hold_time_bars | 19.6709 |
| exposure | 0.4265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
