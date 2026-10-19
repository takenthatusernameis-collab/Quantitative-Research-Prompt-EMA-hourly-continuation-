# EMA Hourly Continuation — APE/USDT P21_89

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.6194 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -3.9413 |
| sortino_ratio | -1.5188 |
| max_drawdown | 0.8476 |
| cagr | -0.5128 |
| net_avg_win | 37.9874 |
| net_avg_loss | -56.8808 |
| avg_hold_time_bars | 10.1989 |
| exposure | 0.3449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
