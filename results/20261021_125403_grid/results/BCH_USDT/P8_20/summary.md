# EMA Hourly Continuation — BCH/USDT P8_20

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6512 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9773 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -2.8233 |
| sortino_ratio | -0.8398 |
| max_drawdown | 0.6326 |
| cagr | -0.3175 |
| net_avg_win | 54.5871 |
| net_avg_loss | -81.5029 |
| avg_hold_time_bars | 6.4112 |
| exposure | 0.1247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
