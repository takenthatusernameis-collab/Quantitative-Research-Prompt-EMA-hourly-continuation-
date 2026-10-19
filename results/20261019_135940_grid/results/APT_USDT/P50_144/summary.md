# EMA Hourly Continuation — APT/USDT P50_144

**Symbol:** APT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.6701 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0035 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -2.5716 |
| sortino_ratio | -0.8045 |
| max_drawdown | 0.6159 |
| cagr | -0.3143 |
| net_avg_win | 51.6129 |
| net_avg_loss | -76.0753 |
| avg_hold_time_bars | 12.4041 |
| exposure | 0.2735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
