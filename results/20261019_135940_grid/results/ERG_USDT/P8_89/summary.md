# EMA Hourly Continuation — ERG/USDT P8_89

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 838 |
| net_profit_factor | 0.4839 |
| net_win_rate | 0.4272 |
| gross_profit_factor | 0.7465 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -6.2332 |
| sortino_ratio | -2.5244 |
| max_drawdown | 0.9560 |
| cagr | -0.7097 |
| net_avg_win | 25.0174 |
| net_avg_loss | -38.5593 |
| avg_hold_time_bars | 15.3998 |
| exposure | 0.5866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
