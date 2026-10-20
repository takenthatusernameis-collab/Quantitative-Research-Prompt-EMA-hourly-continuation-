# EMA Hourly Continuation — ETN/USDT P12_50

**Symbol:** ETN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.3536 |
| net_win_rate | 0.3535 |
| gross_profit_factor | 0.5426 |
| gross_win_rate | 0.3646 |
| sharpe_ratio | -11.5257 |
| sortino_ratio | -5.5935 |
| max_drawdown | 0.9971 |
| cagr | -0.9378 |
| net_avg_win | 15.5815 |
| net_avg_loss | -24.1005 |
| avg_hold_time_bars | 6.1566 |
| exposure | 0.3311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
