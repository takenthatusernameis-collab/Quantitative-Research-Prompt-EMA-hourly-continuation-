# EMA Hourly Continuation — CVX/USDT P12_200

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.9352 |
| net_win_rate | 0.5214 |
| gross_profit_factor | 1.0696 |
| gross_win_rate | 0.5214 |
| sharpe_ratio | -0.2999 |
| sortino_ratio | -0.0720 |
| max_drawdown | 0.2157 |
| cagr | -0.0366 |
| net_avg_win | 88.3415 |
| net_avg_loss | -102.9212 |
| avg_hold_time_bars | 59.3500 |
| exposure | 0.7554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
