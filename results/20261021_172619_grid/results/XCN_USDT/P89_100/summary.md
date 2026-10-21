# EMA Hourly Continuation — XCN/USDT P89_100

**Symbol:** XCN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 100 |
| net_profit_factor | 0.5298 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.7368 |
| gross_win_rate | 0.4200 |
| sharpe_ratio | -2.0268 |
| sortino_ratio | -0.2883 |
| max_drawdown | 0.2978 |
| cagr | -0.1253 |
| net_avg_win | 76.5996 |
| net_avg_loss | -104.7041 |
| avg_hold_time_bars | 7.2800 |
| exposure | 0.0331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
