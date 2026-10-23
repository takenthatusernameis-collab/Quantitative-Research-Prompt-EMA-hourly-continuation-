# EMA Hourly Continuation — ZPAY/USDT P89_144

**Symbol:** ZPAY/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.4278 |
| net_win_rate | 0.3582 |
| gross_profit_factor | 0.5993 |
| gross_win_rate | 0.3602 |
| sharpe_ratio | -5.9875 |
| sortino_ratio | -1.9123 |
| max_drawdown | 0.8977 |
| cagr | -0.5934 |
| net_avg_win | 35.8502 |
| net_avg_loss | -46.7797 |
| avg_hold_time_bars | 11.1667 |
| exposure | 0.2638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
