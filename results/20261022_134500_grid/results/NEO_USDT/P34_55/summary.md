# EMA Hourly Continuation — NEO/USDT P34_55

**Symbol:** NEO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.3013 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.7215 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -9.4239 |
| sortino_ratio | -4.0892 |
| max_drawdown | 0.9943 |
| cagr | -0.8715 |
| net_avg_win | 10.7987 |
| net_avg_loss | -26.6466 |
| avg_hold_time_bars | 3.4211 |
| exposure | 0.1448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
