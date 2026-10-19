# EMA Hourly Continuation — SEI/USDT P20_200

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.9139 |
| net_win_rate | 0.5529 |
| gross_profit_factor | 1.2161 |
| gross_win_rate | 0.5529 |
| sharpe_ratio | -0.4721 |
| sortino_ratio | -0.1245 |
| max_drawdown | 0.2908 |
| cagr | -0.0605 |
| net_avg_win | 81.9357 |
| net_avg_loss | -110.8849 |
| avg_hold_time_bars | 42.5235 |
| exposure | 0.6572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
