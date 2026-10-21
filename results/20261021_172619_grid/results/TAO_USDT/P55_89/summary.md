# EMA Hourly Continuation — TAO/USDT P55_89

**Symbol:** TAO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.7674 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9671 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.2142 |
| sortino_ratio | -0.2800 |
| max_drawdown | 0.3021 |
| cagr | -0.1214 |
| net_avg_win | 70.9688 |
| net_avg_loss | -91.7661 |
| avg_hold_time_bars | 7.6178 |
| exposure | 0.0897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
