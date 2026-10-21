# EMA Hourly Continuation — NEO/USDT P34_200

**Symbol:** NEO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.6852 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.8572 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -1.8631 |
| sortino_ratio | -0.4652 |
| max_drawdown | 0.4536 |
| cagr | -0.1930 |
| net_avg_win | 62.4872 |
| net_avg_loss | -81.1304 |
| avg_hold_time_bars | 35.5130 |
| exposure | 0.4972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
