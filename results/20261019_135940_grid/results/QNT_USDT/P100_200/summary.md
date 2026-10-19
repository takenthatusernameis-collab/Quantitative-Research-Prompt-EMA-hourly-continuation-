# EMA Hourly Continuation — QNT/USDT P100_200

**Symbol:** QNT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6487 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0188 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -2.6253 |
| sortino_ratio | -0.7669 |
| max_drawdown | 0.5926 |
| cagr | -0.3006 |
| net_avg_win | 51.1356 |
| net_avg_loss | -80.7112 |
| avg_hold_time_bars | 9.4444 |
| exposure | 0.1816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
