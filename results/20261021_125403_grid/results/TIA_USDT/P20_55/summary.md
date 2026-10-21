# EMA Hourly Continuation — TIA/USDT P20_55

**Symbol:** TIA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.9300 |
| net_win_rate | 0.5380 |
| gross_profit_factor | 1.1539 |
| gross_win_rate | 0.5380 |
| sharpe_ratio | -0.4593 |
| sortino_ratio | -0.1486 |
| max_drawdown | 0.3226 |
| cagr | -0.0720 |
| net_avg_win | 84.5870 |
| net_avg_loss | -105.9121 |
| avg_hold_time_bars | 8.9820 |
| exposure | 0.2041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
