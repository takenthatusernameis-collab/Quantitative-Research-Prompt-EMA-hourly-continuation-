# EMA Hourly Continuation — XTZ/USDT P12_100

**Symbol:** XTZ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.7861 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.5829 |
| sortino_ratio | -0.4925 |
| max_drawdown | 0.4505 |
| cagr | -0.2036 |
| net_avg_win | 67.2117 |
| net_avg_loss | -87.7168 |
| avg_hold_time_bars | 27.6191 |
| exposure | 0.5900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
