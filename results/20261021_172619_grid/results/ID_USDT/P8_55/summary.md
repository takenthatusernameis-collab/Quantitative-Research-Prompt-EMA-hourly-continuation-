# EMA Hourly Continuation — ID/USDT P8_55

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.7703 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9961 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -2.3539 |
| sortino_ratio | -0.8739 |
| max_drawdown | 0.6758 |
| cagr | -0.3316 |
| net_avg_win | 64.0574 |
| net_avg_loss | -80.7416 |
| avg_hold_time_bars | 16.2271 |
| exposure | 0.4979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
