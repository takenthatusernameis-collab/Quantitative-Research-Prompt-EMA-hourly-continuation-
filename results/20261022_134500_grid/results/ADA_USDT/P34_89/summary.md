# EMA Hourly Continuation — ADA/USDT P34_89

**Symbol:** ADA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.4795 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8427 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -5.5526 |
| sortino_ratio | -2.0243 |
| max_drawdown | 0.9225 |
| cagr | -0.6353 |
| net_avg_win | 27.0082 |
| net_avg_loss | -48.0606 |
| avg_hold_time_bars | 7.0220 |
| exposure | 0.2177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
