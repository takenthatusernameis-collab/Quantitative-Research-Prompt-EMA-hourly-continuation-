# EMA Hourly Continuation — STX/USDT P8_55

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1034 |
| net_profit_factor | 0.5753 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.9030 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -5.7856 |
| sortino_ratio | -2.5986 |
| max_drawdown | 0.9611 |
| cagr | -0.7178 |
| net_avg_win | 27.1712 |
| net_avg_loss | -40.6057 |
| avg_hold_time_bars | 10.5687 |
| exposure | 0.4945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
