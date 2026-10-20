# EMA Hourly Continuation — EDU/USDT P8_12

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1816 |
| net_profit_factor | 0.2467 |
| net_win_rate | 0.3744 |
| gross_profit_factor | 0.6880 |
| gross_win_rate | 0.4146 |
| sharpe_ratio | -15.6445 |
| sortino_ratio | -9.5300 |
| max_drawdown | 1.0000 |
| cagr | -0.9918 |
| net_avg_win | 4.8170 |
| net_avg_loss | -11.6862 |
| avg_hold_time_bars | 2.3420 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
