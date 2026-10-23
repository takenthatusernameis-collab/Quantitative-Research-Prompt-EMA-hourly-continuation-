# EMA Hourly Continuation — ONE/USDT P8_89

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.6857 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.9596 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -3.7386 |
| sortino_ratio | -1.3404 |
| max_drawdown | 0.8120 |
| cagr | -0.4739 |
| net_avg_win | 57.2678 |
| net_avg_loss | -73.4101 |
| avg_hold_time_bars | 22.9969 |
| exposure | 0.6815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
