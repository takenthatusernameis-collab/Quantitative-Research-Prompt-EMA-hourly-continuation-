# EMA Hourly Continuation — BSV/USDT P21_89

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 798 |
| net_profit_factor | 0.4981 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 0.8408 |
| gross_win_rate | 0.4398 |
| sharpe_ratio | -6.7897 |
| sortino_ratio | -2.6890 |
| max_drawdown | 0.9648 |
| cagr | -0.7322 |
| net_avg_win | 28.2067 |
| net_avg_loss | -41.8220 |
| avg_hold_time_bars | 10.7782 |
| exposure | 0.3910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
