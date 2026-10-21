# EMA Hourly Continuation — AXL/USDT P50_144

**Symbol:** AXL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.6872 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8464 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -2.5961 |
| sortino_ratio | -0.7649 |
| max_drawdown | 0.6066 |
| cagr | -0.2972 |
| net_avg_win | 65.7139 |
| net_avg_loss | -79.8240 |
| avg_hold_time_bars | 13.9515 |
| exposure | 0.2734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
