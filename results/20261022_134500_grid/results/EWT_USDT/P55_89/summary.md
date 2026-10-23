# EMA Hourly Continuation — EWT/USDT P55_89

**Symbol:** EWT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.3718 |
| net_win_rate | 0.3932 |
| gross_profit_factor | 0.6828 |
| gross_win_rate | 0.4061 |
| sharpe_ratio | -7.6635 |
| sortino_ratio | -2.6967 |
| max_drawdown | 0.9688 |
| cagr | -0.7439 |
| net_avg_win | 23.5618 |
| net_avg_loss | -41.0632 |
| avg_hold_time_bars | 4.4984 |
| exposure | 0.1264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
