# EMA Hourly Continuation — MEW/USDT P12_200

**Symbol:** MEW/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6964 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.0777 |
| sortino_ratio | -0.5466 |
| max_drawdown | 0.5123 |
| cagr | -0.2304 |
| net_avg_win | 66.1880 |
| net_avg_loss | -85.8016 |
| avg_hold_time_bars | 47.5795 |
| exposure | 0.7613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
