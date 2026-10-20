# EMA Hourly Continuation — WAVES/USDT P89_144

**Symbol:** WAVES/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.3901 |
| net_win_rate | 0.4077 |
| gross_profit_factor | 0.7800 |
| gross_win_rate | 0.4303 |
| sharpe_ratio | -7.2173 |
| sortino_ratio | -2.4384 |
| max_drawdown | 0.9596 |
| cagr | -0.7158 |
| net_avg_win | 26.1744 |
| net_avg_loss | -46.1779 |
| avg_hold_time_bars | 4.8467 |
| exposure | 0.1265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
