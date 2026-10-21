# EMA Hourly Continuation — UNI/USDT P21_144

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8715 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0416 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -0.7516 |
| sortino_ratio | -0.1979 |
| max_drawdown | 0.2903 |
| cagr | -0.0894 |
| net_avg_win | 82.1753 |
| net_avg_loss | -99.4686 |
| avg_hold_time_bars | 32.3442 |
| exposure | 0.4955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
