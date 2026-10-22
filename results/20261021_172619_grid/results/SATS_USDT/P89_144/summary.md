# EMA Hourly Continuation — SATS/USDT P89_144

**Symbol:** SATS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.6039 |
| net_win_rate | 0.4407 |
| gross_profit_factor | 0.7978 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -2.5742 |
| sortino_ratio | -0.5993 |
| max_drawdown | 0.5158 |
| cagr | -0.2417 |
| net_avg_win | 64.3817 |
| net_avg_loss | -84.0127 |
| avg_hold_time_bars | 8.9778 |
| exposure | 0.1097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
