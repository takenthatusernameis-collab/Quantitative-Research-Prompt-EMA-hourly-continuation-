# EMA Hourly Continuation — AXL/USDT P34_144

**Symbol:** AXL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.7185 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8719 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -2.4786 |
| sortino_ratio | -0.7492 |
| max_drawdown | 0.5974 |
| cagr | -0.2923 |
| net_avg_win | 71.0893 |
| net_avg_loss | -83.7138 |
| avg_hold_time_bars | 17.3904 |
| exposure | 0.3588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
