# EMA Hourly Continuation — HTX/USDT P20_89

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.5167 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.8380 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -5.7303 |
| sortino_ratio | -1.8626 |
| max_drawdown | 0.8933 |
| cagr | -0.5869 |
| net_avg_win | 42.9836 |
| net_avg_loss | -62.8142 |
| avg_hold_time_bars | 17.6957 |
| exposure | 0.4132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
