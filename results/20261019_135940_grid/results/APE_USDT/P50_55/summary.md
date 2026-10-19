# EMA Hourly Continuation — APE/USDT P50_55

**Symbol:** APE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.2164 |
| net_win_rate | 0.3737 |
| gross_profit_factor | 0.7143 |
| gross_win_rate | 0.4343 |
| sharpe_ratio | -12.0693 |
| sortino_ratio | -5.2143 |
| max_drawdown | 0.9991 |
| cagr | -0.9384 |
| net_avg_win | 8.4388 |
| net_avg_loss | -23.2670 |
| avg_hold_time_bars | 1.7577 |
| exposure | 0.0699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
