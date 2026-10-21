# EMA Hourly Continuation — JTO/USDT P12_21

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.8010 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0934 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -1.5493 |
| sortino_ratio | -0.4571 |
| max_drawdown | 0.4776 |
| cagr | -0.1893 |
| net_avg_win | 75.9816 |
| net_avg_loss | -101.4027 |
| avg_hold_time_bars | 4.8167 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
