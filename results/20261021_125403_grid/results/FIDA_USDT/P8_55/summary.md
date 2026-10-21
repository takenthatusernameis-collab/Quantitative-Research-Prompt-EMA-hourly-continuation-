# EMA Hourly Continuation — FIDA/USDT P8_55

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.7767 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 0.9916 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -2.0629 |
| sortino_ratio | -0.7856 |
| max_drawdown | 0.6086 |
| cagr | -0.3039 |
| net_avg_win | 58.5497 |
| net_avg_loss | -75.5903 |
| avg_hold_time_bars | 14.9128 |
| exposure | 0.4798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
