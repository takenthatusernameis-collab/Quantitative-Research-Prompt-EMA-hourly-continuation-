# EMA Hourly Continuation — BCH/USDT P8_34

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1301 |
| net_profit_factor | 0.3679 |
| net_win_rate | 0.4112 |
| gross_profit_factor | 0.8211 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -11.4752 |
| sortino_ratio | -5.8292 |
| max_drawdown | 0.9995 |
| cagr | -0.9514 |
| net_avg_win | 10.8738 |
| net_avg_loss | -20.6429 |
| avg_hold_time_bars | 6.2529 |
| exposure | 0.3698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
