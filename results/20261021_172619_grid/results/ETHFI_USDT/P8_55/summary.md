# EMA Hourly Continuation — ETHFI/USDT P8_55

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.7852 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.8974 |
| sortino_ratio | -0.6825 |
| max_drawdown | 0.5595 |
| cagr | -0.2709 |
| net_avg_win | 64.9922 |
| net_avg_loss | -77.7276 |
| avg_hold_time_bars | 16.0236 |
| exposure | 0.4632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
