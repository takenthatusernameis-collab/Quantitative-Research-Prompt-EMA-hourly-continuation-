# EMA Hourly Continuation — WOO/USDT P8_144

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7653 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 1.0247 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.8746 |
| sortino_ratio | -0.5438 |
| max_drawdown | 0.4991 |
| cagr | -0.2275 |
| net_avg_win | 73.7126 |
| net_avg_loss | -95.8650 |
| avg_hold_time_bars | 40.2624 |
| exposure | 0.7741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
