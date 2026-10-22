# EMA Hourly Continuation — APT/USDT P12_144

**Symbol:** APT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6672 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9607 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -2.3530 |
| sortino_ratio | -0.6340 |
| max_drawdown | 0.5486 |
| cagr | -0.2654 |
| net_avg_win | 60.0284 |
| net_avg_loss | -84.7934 |
| avg_hold_time_bars | 43.1429 |
| exposure | 0.7275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
