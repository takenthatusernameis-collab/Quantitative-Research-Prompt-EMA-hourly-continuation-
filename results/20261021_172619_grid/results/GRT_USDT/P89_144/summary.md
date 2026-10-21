# EMA Hourly Continuation — GRT/USDT P89_144

**Symbol:** GRT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.8151 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.0919 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -1.0218 |
| sortino_ratio | -0.2256 |
| max_drawdown | 0.3016 |
| cagr | -0.0992 |
| net_avg_win | 83.0173 |
| net_avg_loss | -110.8655 |
| avg_hold_time_bars | 8.0339 |
| exposure | 0.0858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
