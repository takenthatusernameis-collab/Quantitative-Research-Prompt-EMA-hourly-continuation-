# EMA Hourly Continuation — KNC/USDT P20_144

**Symbol:** KNC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.6863 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9975 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -2.6083 |
| sortino_ratio | -0.7495 |
| max_drawdown | 0.6260 |
| cagr | -0.3069 |
| net_avg_win | 62.9924 |
| net_avg_loss | -88.8070 |
| avg_hold_time_bars | 31.5106 |
| exposure | 0.6087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
