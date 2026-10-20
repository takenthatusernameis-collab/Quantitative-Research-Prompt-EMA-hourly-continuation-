# EMA Hourly Continuation — RSR/USDT P55_89

**Symbol:** RSR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.5488 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.9047 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -4.8386 |
| sortino_ratio | -1.8058 |
| max_drawdown | 0.8861 |
| cagr | -0.5766 |
| net_avg_win | 33.1061 |
| net_avg_loss | -53.2723 |
| avg_hold_time_bars | 3.8240 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
