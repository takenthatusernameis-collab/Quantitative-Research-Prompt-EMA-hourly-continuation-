# EMA Hourly Continuation — FLR/USDT P12_34

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.5764 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8069 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -4.3697 |
| sortino_ratio | -1.5246 |
| max_drawdown | 0.8320 |
| cagr | -0.5035 |
| net_avg_win | 42.1710 |
| net_avg_loss | -59.2004 |
| avg_hold_time_bars | 6.6734 |
| exposure | 0.1811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
