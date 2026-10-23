# EMA Hourly Continuation — T/USDT P50_200

**Symbol:** T/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5924 |
| net_win_rate | 0.4696 |
| gross_profit_factor | 0.9436 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -2.7941 |
| sortino_ratio | -0.7303 |
| max_drawdown | 0.5829 |
| cagr | -0.2906 |
| net_avg_win | 51.9829 |
| net_avg_loss | -77.6781 |
| avg_hold_time_bars | 26.2406 |
| exposure | 0.4097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
