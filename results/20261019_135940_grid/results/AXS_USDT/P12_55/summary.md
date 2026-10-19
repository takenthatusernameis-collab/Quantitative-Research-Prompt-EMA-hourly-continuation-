# EMA Hourly Continuation — AXS/USDT P12_55

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 941 |
| net_profit_factor | 0.5731 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.9772 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -5.4486 |
| sortino_ratio | -2.3436 |
| max_drawdown | 0.9450 |
| cagr | -0.6768 |
| net_avg_win | 28.2265 |
| net_avg_loss | -44.7599 |
| avg_hold_time_bars | 8.8842 |
| exposure | 0.3783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
