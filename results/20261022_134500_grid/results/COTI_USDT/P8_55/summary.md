# EMA Hourly Continuation — COTI/USDT P8_55

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1115 |
| net_profit_factor | 0.6515 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9886 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -5.2043 |
| sortino_ratio | -2.4403 |
| max_drawdown | 0.9528 |
| cagr | -0.6918 |
| net_avg_win | 33.3795 |
| net_avg_loss | -46.5825 |
| avg_hold_time_bars | 9.4350 |
| exposure | 0.4782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
