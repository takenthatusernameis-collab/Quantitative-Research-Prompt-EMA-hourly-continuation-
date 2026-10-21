# EMA Hourly Continuation — MLK/USDT P12_89

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.5889 |
| net_win_rate | 0.4137 |
| gross_profit_factor | 0.7830 |
| gross_win_rate | 0.4174 |
| sharpe_ratio | -4.4304 |
| sortino_ratio | -1.4516 |
| max_drawdown | 0.8233 |
| cagr | -0.4899 |
| net_avg_win | 52.4753 |
| net_avg_loss | -62.8853 |
| avg_hold_time_bars | 18.2208 |
| exposure | 0.4444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
